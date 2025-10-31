import { useState } from 'react'
import './input.css'
import { IoIosSend } from "react-icons/io";


export default function ChatInput(){
    const [query, setQuery] = useState("")

    return (
        <div className="chat-input">
            <form 
            className="chat-input-form"
            >
                
            <textarea 
            className="chat-input-textarea" 
            type="text" 
            placeholder="Type your message here..." 
            onChange = {e => setQuery(e.target.value)} 
            value={query}
            />
            <button 
            className="chat-input-button" 
            type="submit"
            onClick={() => onSend({message: query})}
            disabled={!query.trim()}
            >
                <IoIosSend size={30} color="#ffffff"/>
            </button>
            </form>
    </div>
  );
}

function onSend(props){
    return(
        alert(props.message)
    )
}