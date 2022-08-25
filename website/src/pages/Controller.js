// This react.js file is presenting a link for Controller page.

// import css file for this Controller.js file
import './Controller.css';

// When clike the link for Controller, the webpage displays a link for showing controlling live video.
const Controller = () => {
  return (
    
    <div className = 'Controller'>
    
    <header className = 'Controller-header'>
      <h1>Controller</h1>
      <div>
          <p>
            <a
          className="App-link"
          href="http://192.168.137.76:8000"
          target="_blank"
          rel="noopener noreferrer"
        >
          CLICK HERE
          <p></p>
        </a></p>
          
      </div>

    </header>
  </div>
  );
};
  
  export default Controller;