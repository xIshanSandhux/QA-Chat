import { useState } from 'react'
import './input.css'
import { IoIosSend } from "react-icons/io";
import axios from 'axios';
import Cookies from 'js-cookie';

export default function ChatInput(){
    const [query, setQuery] = useState("")
    const sessionId = Cookies.get('sessionId');
    return (
        <div className="chat-input">
            <form
            name="chat-input-form"
            className="chat-input-form"
            onSubmit = {(e)=>{
                e.preventDefault();
                onSend({message: query, sesId: sessionId});
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
            sessionId: props.sesId
        });
        alert(queryRes.data.chatResponse);
    }
    catch(error){
        console.error('Error:', error);
    }
}