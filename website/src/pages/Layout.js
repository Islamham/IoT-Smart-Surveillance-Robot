// This react.js file is link layout

//import css file
import './Layout.css';

// import for using react-router
import { Outlet} from "react-router-dom";

// displaying links to other react.js files. 
const Layout = () => {
  return (
    <>
      <nav>
        <ul className="Layout-header">

          {/* link for move to Home react.js file  */}
          <a
          className="Layout-b4"
          href="http://cpen291-5.ece.ubc.ca/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Home
          <p></p>
        </a>

        {/* link for move to About react.js file */}
        <a
          className="Layout-b3"
          href="http://cpen291-5.ece.ubc.ca/About"
          target="_blank"
          rel="noopener noreferrer"
        >
          About
          <p></p>
        </a>

        {/* link for move to Camera react.js file */}
        <a
          className="Layout-b2"
          href="http://cpen291-5.ece.ubc.ca/Controller"
          target="_blank"
          rel="noopener noreferrer"
        >
          Controller
          <p></p>
        </a>

        {/* link for move to Logs react.js file */}
        <a
          className="Layout-b1"
          href="http://cpen291-5.ece.ubc.ca/Objd"
          target="_blank"
          rel="noopener noreferrer"
        >
          Object detection
        </a>



        </ul>
      </nav>
      <Outlet />
    </>
  )
};

export default Layout;

