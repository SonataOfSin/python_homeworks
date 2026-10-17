
var apiUrl = "https://jsonplaceholder.typicode.com/todos";
var allTodos = [];       // აქ ჩავალაგებთ ყველა todo-ს API-დან
var filteredTodos = [];  // ეს არის ის todos, რაც რჩება ფილტრის/ძებნის შემდეგ
var currentPage = 1;
var itemsPerPage = 10;
var boardDiv = document.getElementById("board");
var paginationDiv = document.getElementById("pagination");
var resultCountSpan = document.getElementById("resultCount");
var searchInput = document.getElementById("searchInput");
var userSelect = document.getElementById("userSelect");
var statusSelect = document.getElementById("statusSelect");
var resetBtn = document.getElementById("resetBtn");

// გვერდის ჩატვირთვისას წამოვიღოთ todos
fetch(apiUrl)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    allTodos = data;
    fillUserDropdown();
    filterTodos();
  })
  .catch(function (error) {
    boardDiv.innerHTML = "<p class='error'>შეცდომა მონაცემების წამოღებისას: " + error + "</p>";
  });

// userId-ების dropdown-ის შევსება (1-დან 10-მდე იქნება ჩვეულებრივ)
function fillUserDropdown() {
  var usedIds = [];
  for (var i = 0; i < allTodos.length; i++) {
    var id = allTodos[i].userId;
    if (usedIds.indexOf(id) === -1) {
      usedIds.push(id);
    }
  }
  usedIds.sort(function (a, b) { return a - b; });

  for (var j = 0; j < usedIds.length; j++) {
    var option = document.createElement("option");
    option.value = usedIds[j];
    option.textContent = usedIds[j];
    userSelect.appendChild(option);
  }
}

// ფილტრაცია + ძებნა ერთად
function filterTodos() {
  var searchText = searchInput.value.toLowerCase();
  var selectedUser = userSelect.value;
  var selectedStatus = statusSelect.value;

  filteredTodos = allTodos.filter(function (todo) {
    var matchesSearch = todo.title.toLowerCase().indexOf(searchText) !== -1;
    var matchesUser = selectedUser === "" || todo.userId == selectedUser;
    var matchesStatus = selectedStatus === "" || String(todo.completed) === selectedStatus;

    return matchesSearch && matchesUser && matchesStatus;
  });

  currentPage = 1;
  renderTodos();
}

// ივენთები ფილტრებზე
searchInput.addEventListener("keyup", filterTodos);
userSelect.addEventListener("change", filterTodos);
statusSelect.addEventListener("change", filterTodos);

resetBtn.addEventListener("click", function () {
  searchInput.value = "";
  userSelect.value = "";
  statusSelect.value = "";
  filterTodos();
});

// todos-ის დახატვა გვერდზე (მხოლოდ title + პატარა info)
function renderTodos() {
  resultCountSpan.textContent = filteredTodos.length;

  if (filteredTodos.length === 0) {
    boardDiv.innerHTML = "<p class='empty'>todo ვერ მოიძებნა :(</p>";
    paginationDiv.innerHTML = "";
    return;
  }

  var startIndex = (currentPage - 1) * itemsPerPage;
  var endIndex = startIndex + itemsPerPage;
  var pageTodos = filteredTodos.slice(startIndex, endIndex);

  var html = "<ul id='todoList'>";

  for (var i = 0; i < pageTodos.length; i++) {
    var todo = pageTodos[i];
    var statusClass = todo.completed ? "done" : "not-done";
    var statusText = todo.completed ? "DONE" : "NOT DONE";

    html += "<li onclick=\"goToDetail(" + todo.id + ")\">";
    html += "<span class='todo-id'>#" + todo.id + "</span>";
    html += "<span class='todo-user'>user " + todo.userId + "</span>";
    html += "<span class='todo-title'>" + todo.title + "</span>";
    html += "<span class='" + statusClass + "'>" + statusText + "</span>";
    html += "</li>";
  }

  html += "</ul>";
  boardDiv.innerHTML = html;

  renderPagination();
}

// გადასვლა დეტალურ გვერდზე
function goToDetail(id) {
  window.location.href = "todo.html?id=" + id;
}

// პაგინაციის ღილაკები
function renderPagination() {
  var totalPages = Math.ceil(filteredTodos.length / itemsPerPage);
  var html = "";

  // წინა ღილაკი
  html += "<button onclick='changePage(" + (currentPage - 1) + ")' " + (currentPage === 1 ? "disabled" : "") + ">Prev</button>";

  for (var p = 1; p <= totalPages; p++) {
    if (p === currentPage) {
      html += "<button class='active' onclick='changePage(" + p + ")'>" + p + "</button>";
    } else {
      html += "<button onclick='changePage(" + p + ")'>" + p + "</button>";
    }
  }

  // შემდეგი ღილაკი
  html += "<button onclick='changePage(" + (currentPage + 1) + ")' " + (currentPage === totalPages ? "disabled" : "") + ">Next</button>";

  paginationDiv.innerHTML = html;
}

function changePage(page) {
  currentPage = page;
  renderTodos();
  window.scrollTo(0, 0);
}
