// main.js is app.js
import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

// const app = Vue.createApp({template: '<h1>hello {{fname}}</h1>',
// data() {return {fname:'testfname'}} }
// )
//app.$mount('#app')

// existing code

new Vue({
  render: h => h(App),
}).$mount('#app')
