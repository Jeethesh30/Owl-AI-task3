const form = document.getElementById("task-form")
const taskInput = document.getElementById("task-input")
const dueDateInput = document.getElementById("due-date-input")
const noteInput = document.getElementById("note-input")
const priorityInput = document.getElementById("priority-input")

const taskList = document.getElementById("task-list")

const searchInput = document.getElementById("search-input")
const sortSelect = document.getElementById("sort-select")

let tasks = []


async function getTasks(){

const res = await fetch("/api/tasks")

tasks = await res.json()

renderTasks()

}


async function addTask(title,due,note,priority){

await fetch("/api/tasks",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({

title:title,
due_date:due,
note:note,
priority:priority

})

})

}


async function deleteTask(id){

await fetch("/api/tasks/"+id,{

method:"DELETE"

})

}


async function toggleTask(id){

await fetch("/api/tasks/"+id+"/toggle",{

method:"POST"

})

}


form.addEventListener("submit",async function(e){

e.preventDefault()

await addTask(

taskInput.value,
dueDateInput.value,
noteInput.value,
priorityInput.value

)

taskInput.value=""
dueDateInput.value=""
noteInput.value=""

getTasks()

})


searchInput.addEventListener("input",async function(e){

const q=e.target.value

if(q){

const res=await fetch("/api/search?q="+q)

tasks=await res.json()

renderTasks()

}else{

getTasks()

}

})


sortSelect.addEventListener("change",async function(e){

const res=await fetch("/api/sort",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({

by:e.target.value

})

})

tasks=await res.json()

renderTasks()

})


function renderTasks(){

taskList.innerHTML=""

tasks.forEach(function(task){

const li=document.createElement("li")

if(task.completed){

li.classList.add("completed")

}

if(task.due_date){

const today=new Date().toISOString().split("T")[0]

if(task.due_date<today){

li.classList.add("overdue")

}

}

li.innerHTML=`

<input type="checkbox" ${task.completed?"checked":""}>

<span>[${task.priority}] ${task.title}</span>

<span>${task.due_date||""}</span>

<button>Remove</button>

`

li.querySelector("input").onclick=async function(){

await toggleTask(task.id)

getTasks()

}

li.querySelector("button").onclick=async function(){

await deleteTask(task.id)

getTasks()

}

taskList.appendChild(li)

})

}

getTasks()