// This file is an react.js file for presenting About page, which has explanation of our project and images of the car.

//import image files of our robot.
// import img1 from "./img1.jpg";
// import img2 from "./img2.jpg";
// import img3 from "./img3.jpg";
// import img4 from "./IMG_3778.jpg";
// import img5 from "./IMG_3779.jpg";

// import css file for this About.js file
import './About.css';

// Display title, which is 'About', and explanation of our project, and five images of our car.
const About = () => {
    return (
    <div className = "About">
      
      <header className = "About-header">
        <h1>About</h1>
        <div>
            <p>A car robot with attached camera is controlled remotely by website. The robot detects people and objects while moving around, and it has machine learning functionality for identifying detected objects based on databases. The robot logs information about the objects it detects on the website. Additional implementation featuring data is to be decided on.</p>
            <span><br></br></span>
            <div>
                {/* <img src={img1} alt="image1" width ="300" height = "200" /> */}
                {/* <img src={img2} alt="image2" width ="300" height = "200"/>
                <img src={img3} alt="image3" width ="300" height = "200"/>

                <span><br></br></span>
                <img src={img4} alt="image3" width ="200" height = "300"/>
                <img src={img5} alt="image3" width ="200" height = "300"/> */}
                
            </div>
        </div>
        
        
        
      </header>
    </div>
    );
  };
  
  export default About;