import { createRouter, createWebHistory } from "vue-router";
import App from "../App.vue";
import Dashboard from "../Dashboard.vue";
import Home from "../Home.vue";
import LoginSignUp from "../components/LoginSignUp.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [{ path: "/", component: LoginSignUp },
    {path: "/dashboard", component: Dashboard},
    {path: "/home", component: Home}
  ]
});

export default router;
