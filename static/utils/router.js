import Login from "../pages/Login.js";
import Home from "../pages/home.js";
import Profile from "../pages/Profile.js";
import Signup from "../pages/Signup.js";
import DashboardAdmin from "../pages/DashboardAdmin.js";
import DashboardInfluencer from "../pages/DashboardInfluencer.js";
import DashboardSponsor from "../pages/DashboardSponsor.js";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/profile", component: Profile },
  { path: "/signup", component: Signup },
  { path: "/admin-dashboard", component: DashboardAdmin },
  { path: "/influ-dashboard", component: DashboardInfluencer },
  { path: "/spon-dashboard", component: DashboardSponsor },
];

const router = new VueRouter({
  routes,
});

export default router;
