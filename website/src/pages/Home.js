// This react.js file is presenting Home page which has links to Home itself, About, Controller, object detection. 

// import for using react-router
import { Outlet } from "react-router-dom";

// import svg file of a robot.
import logo from './Robot1.svg';


//import css file
import './Home.css';

// displaying title of this project and logo. 
const Home = () => {
  return (
    <>
      <div className="Home">
        {/* disply header and logo  */}
        <header className="Home-header">
          <h1>WALLE - SE</h1>
          <span><br></br></span>
          <img src={logo} className="Home-logo" alt="logo" />
          <span><br></br></span>
          <p>
          <nav>

      </nav>

      <Outlet />
  
          </p>
          
        </header>
      </div>
    
    
      
    </>
  )
};

export default Home;

