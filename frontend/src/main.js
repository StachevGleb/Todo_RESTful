import Vue from "vue";
import myApp from "./App.vue";
import router from "./router";
// install bootstrap first
import 'bootstrap/dist/css/bootstrap.css';
// Importing the bootstrapvue library
import BootstrapVue from 'bootstrap-vue';


Vue.config.productionTip = false;
Vue.use(BootstrapVue)

new Vue({
  router,
  render: (h) => h(myApp),
}).$mount("#app");