import "./assets/main.css";
import "./style.css";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/router.js";
import state from "./state/state.js";

const app = createApp(App);

app.use(router);
app.use(state);
app.mount("#app");
