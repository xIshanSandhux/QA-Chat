import { useState } from 'react'
import './input.css'
import { IoIosSend } from "react-icons/io";
import axios from 'axios';

export default function ChatInput(){
    const [query, setQuery] = useState("")

    return (
        <div className="chat-input">
            <form
            name="chat-input-form"
            className="chat-input-form"
            onSubmit = {(e)=>{
                e.preventDefault();
                onSend({message: query});
                setQuery('');
            }}
            >
                
            <textarea 
            className="chat-input-textarea" 
            name="chat-input-textarea"
            type="text" 
            placeholder="Type your message here..." 
            onChange = {e => setQuery(e.target.value)} 
            value={query}
            />
            <button 
            className="chat-input-button" 
            type="submit"
            // onClick={() => onSend({message: query})}
            disabled={!query.trim()}
            >
                <IoIosSend size={30} color="#ffffff"/>
            </button>
            </form>
    </div>
  );
}

async function onSend(props){

    try {
        const queryRes = await axios.post('http://127.0.0.1:8000/chatResponse', {
            currentQuery: props.message,
            sessionId: 'test-session-id'
        });
        alert(queryRes.data.chatResponse);
    }
    catch(error){
        console.error('Error:', error);
    }
}