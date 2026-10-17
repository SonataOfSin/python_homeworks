// ------------------------------
// Todo Detail Page - todo.js
// ------------------------------

var apiUrl = "https://jsonplaceholder.typicode.com/todos";
var detailDiv = document.getElementById("detail");

// წამოვიღოთ id-ს URL-იდან, მაგ todo.html?id=5
var params = new URLSearchParams(window.location.search);
var todoId = params.get("id");

if (!todoId) {
  detailDiv.innerHTML = "<p class='error'>id არ არის მითითებული URL-ში</p>";
} else {
  fetch(apiUrl + "/" + todoId)
    .then(function (response) {
      return response.json();
    })
    .then(function (todo) {
      if (!todo.id) {
        detailDiv.innerHTML = "<p class='error'>todo ვერ მოიძებნა</p>";
        return;
      }

      var statusText = todo.completed ? "true (დასრულებული)" : "false (არადასრულებული)";

      var html = "<div class='detail-box'>";
      html += "<p><b>ID:</b> " + todo.id + "</p>";
      html += "<p><b>User ID:</b> " + todo.userId + "</p>";
      html += "<p><b>Title:</b> " + todo.title + "</p>";
      html += "<p><b>Completed:</b> " + statusText + "</p>";
      html += "</div>";

      detailDiv.innerHTML = html;
    })
    .catch(function (error) {
      detailDiv.innerHTML = "<p class='error'>შეცდომა: " + error + "</p>";
    });
}
