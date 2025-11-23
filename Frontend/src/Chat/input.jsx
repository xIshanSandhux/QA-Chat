import { useState } from 'react'
import './input.css'
import { IoIosSend } from "react-icons/io";
import axios from 'axios';
import Cookies from 'js-cookie';

export default function ChatInput({setMessage, allMessages, webSearch}){
    const [query, setQuery] = useState("")
    const sessionId = Cookies.get('sessionId');
    
    return (
        <div className="chat-input">
            <form
            name="chat-input-form"
            className="chat-input-form"
            onSubmit = {(e)=>{
                e.preventDefault();
                const newMessages = [...allMessages, {role: 'user', message: query}];
                setMessage(newMessages);
                onSend({message: query, sesId: sessionId, messages: newMessages, setMessage: setMessage, search: webSearch});
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
            sessionId: props.sesId,
            webSearch: props.search
        });
        props.setMessage([...props.messages, {role: 'assistant', message: queryRes.data.chatResponse}]);
    }
    catch(error){
        console.error('Error:', error);
    }
}