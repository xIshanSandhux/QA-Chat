import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ChatInput from './Chat/input'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <ChatInput />
      
    </>
  )
}

export default App
