import os
from typing import Any

import httpx
import streamlit as st


DEFAULT_API_BASE_URL = "http://localhost:8000"
REQUEST_TIMEOUT = httpx.Timeout(180.0, connect=10.0)


def api_base_url() -> str:
    return os.getenv("API_BASE_URL", DEFAULT_API_BASE_URL).rstrip("/")


def create_plan(user_request: str) -> dict[str, Any]:
    try:
        response = httpx.post(
            f"{api_base_url()}/api/travel-plan",
            json={"request": user_request},
            timeout=REQUEST_TIMEOUT,
        )
    except httpx.TimeoutException as exc:
        raise RuntimeError(
            "The planner request timed out. The agents may still be working; "
            "check the API server before submitting again."
        ) from exc
    except httpx.RequestError as exc:
        raise RuntimeError(
            f"Could not connect to the API at {api_base_url()}. "
            "Start FastAPI and check API_BASE_URL."
        ) from exc

    if not response.is_success:
        try:
            detail = response.json().get("detail", response.text)
        except ValueError:
            detail = response.text
        raise RuntimeError(f"API returned HTTP {response.status_code}: {detail}")

    try:
        result = response.json()
    except ValueError as exc:
        raise RuntimeError("The API returned an invalid JSON response.") from exc

    if not isinstance(result, dict):
        raise RuntimeError("The API returned a response in an unexpected format.")
    return result


def main() -> None:
    st.set_page_config(
        page_title="Multi-Agent Travel Planner",
        page_icon="✈️",
        layout="wide",
    )
    st.title("✈️ Multi-Agent Travel Planner")
    st.write(
        "Describe your trip and let destination, local food, and budget "
        "specialists work together to create a practical plan."
    )

    with st.sidebar:
        st.subheader("FastAPI service")
        st.code(api_base_url())
        st.caption("Set API_BASE_URL in the environment to use another server.")
        st.link_button("Open API documentation", f"{api_base_url()}/docs")

    with st.form("travel_request_form"):
        user_request = st.text_area(
            "What kind of trip would you like to plan?",
            height=150,
            placeholder=(
                "For example: I want to spend 4 days in Paris, "
                "visit museums, try local food, and keep a moderate budget."
            ),
        )
        submitted = st.form_submit_button("Create travel plan", type="primary")

    if submitted:
        if not user_request.strip():
            st.warning("Describe your trip before submitting.")
        else:
            try:
                with st.spinner(
                    "The three specialists are preparing recommendations..."
                ):
                    st.session_state.travel_plan = create_plan(user_request.strip())
            except RuntimeError as exc:
                st.error(str(exc))

    plan = st.session_state.get("travel_plan")
    if plan:
        st.divider()
        st.header("Your travel plan")
        st.markdown(plan["final_plan"])

        with st.expander("Specialist recommendations"):
            tab_destination, tab_food, tab_budget = st.tabs(
                ["Destination & activities", "Local food", "Budget"]
            )
            with tab_destination:
                st.markdown(plan["destination_info"])
            with tab_food:
                st.markdown(plan["food_info"])
            with tab_budget:
                st.markdown(plan["budget_info"])
                st.caption(
                    "Budget figures are model-generated estimates, "
                    "not live prices."
                )


if __name__ == "__main__":
    main()
