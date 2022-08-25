// This react.js file is presenting a link for object detection. 

// import css file for this Objd.js file
import './Objd.css';

// When the object detection link is clicked, the poped up page displays a link for other website for object detection.
const Objd = () => {
    return (
      <div className = 'Objd'>
      
      <header className = 'Objd-header'>
        <h1>Object Detection</h1>
        <div>
            <p>
              This link opens a page which is for object detection.
            <a
          className="App-link"
          href="http://127.0.0.1:5000/"
          target="_blank"
          rel="noopener noreferrer"
        >
          CLICK HERE
          <p></p>
        </a>
            </p>
            
        </div>

      </header>
    </div>
    );
  };
  
  export default Objd;