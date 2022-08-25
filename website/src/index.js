// This file is for displaying react.js files.

// import for using react.js
import ReactDOM from "react-dom";

// import for using react-router
import { BrowserRouter, Routes, Route } from "react-router-dom";

// import other React.js files from pages folder
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import About from "./pages/About";
import Controller from "./pages/Controller";
import Objd from "./pages/Objd";
import NoPage from "./pages/NoPage";

// open each react.js file based on the dedicated path.
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
      <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="About" element={<About />} />
          <Route path="Controller" element={<Controller />} />
          <Route path="Objd" element={<Objd />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
