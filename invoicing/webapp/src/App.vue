<template>
  <div class="container">
    <!-- <div id="app"> -->
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <Header
      @toggle-add-profile="toggleAddProfile"
      title="Business Profiles"
      :showAddProfile="showAddProfile"
    />
    <div>
      <AddProfile v-show="showAddProfile" @add-profile="addProfile" />
    </div>
    <Tasks @delete-task="deleteTask" :tasks="tasks" />

    <!-- <HelloWorld msg="changing the text to test"/> -->
    <!-- </div> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Header from "./components/Header";
import Tasks from "./components/Tasks";
import AddProfile from "./components/AddProfile";
export default {
  name: "App",
  // components: { HelloWorld  }
  components: { Header, Tasks, AddProfile },
  data() {
    return { tasks: [], showAddProfile: false };
  },
  methods: {
    deleteTask(id) {
      this.tasks = this.tasks.filter((task) => task.id !== id);

      fetch("/task/delete_task/" + id, {
        method: "DELETE",
        headers: {
          //'Accept': 'application/json',
          "Content-Type": "application/json",
        },
        body: JSON.stringify(id),
      });
    },
    updateTask(task) {
      //this.tasks = this.tasks.filter((task) => task.id !== id);
      fetch("127.0.0.1:8000/task/update_task/" + task.id, {
        method: "PUT",
        headers: {
          //'Accept': 'application/json',
          "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
      });
    },
    addProfile(task) {
      // if (confirm('Are you sure?'))
      //this.tasks=[...this.tasks, task]
      fetch("http://127.0.0.1:8000/task/create_task", {
        method: "POST",
        headers: {
          //'Accept': 'application/json',
          "Content-Type": "application/json",
        },
        body: JSON.stringify(task),
      });
    },
    toggleAddProfile() {
      this.showAddProfile = !this.showAddProfile;
    },
  },
  //   created(){

  //   this.tasks = [
  //       ]
  // },
  // {id:1,text:'Jon', business:'ABC Ltd',address:'Main st', taxid:1},
  // {id:2,text:'Tom', business:'XYZ Ltd',address:'Sim st',taxid:2},

  mounted() {
    let fetchRes = fetch("http://127.0.0.1:8000/task");
    fetchRes
      .then((res) => res.json())
      .then((data) => {
        this.tasks = this.tasks.concat(data.tasks);
      });
  },
};
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: "Poppins", sans-serif;
}
.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
<!--
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: green;
  margin-top: 60px;
}
</style>
-->
