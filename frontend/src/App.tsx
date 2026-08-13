import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'


// user enters the prompt 
    // the prompt is saved in the state 
    // the user clicks analyze button 
    // analyzePrompt() runs 
    // send prompt to FastAPi 
    // fastAPI connects the python pipeline 
    // the results are sent back from the fastAPI 
    // setLlmAnswer is changed

function App() {
  const [llmAnswer, setLlmAnswer] = useState("")
  


  function analyzePrompt(){
    //once the button is clicked this function will run 
    //the prompt typed should be sent to the the FastAPI which will inturn send it to the backend

    
  }

  return (
    <div>
      <h1>AI Safety Risk Analysis</h1>
      <input type="text" id="inputPrompt" placeholder="Enter prompt " style={{ width: '300px' }} />
      <br />
      <button type="button" onClick={analyzePrompt}>Analyze</button>
      <br/>
      <div>The answer from the llm is {llmAnswer}</div>



    </div>
   

  )
}

export default App
