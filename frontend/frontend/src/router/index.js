import Vue from "vue";
import VueRouter from "vue-router";
import Test from "../components/Test.vue";
import Tasks from "../components/Tasks.vue"

Vue.use(VueRouter);

 

const routes = [
  {
    path: "/test",
    name: "Test",
    component: Test,
  },
  {
    path: "/tasks",
    name: "Tasks",
    component: Tasks,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

