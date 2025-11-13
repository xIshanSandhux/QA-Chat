import { useEffect, useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import ChatInput from './input';
import MessageDisplay from './messageDisplay';
import Search from '../webSearch/search';

let ran = false;
export default function ChatMain(){

  const [messages, setMessages] = useState([]);
  const [webSearch, setWebSearch] = useState(false);

    useEffect(()=>{
    let sessionId;
    if (!ran){
      ran = true;
      const fetchSessionId = async () => {
        try{
          sessionId = await getSessionId();
          Cookies.set('sessionId', sessionId)
        }catch(error){
          console.error('Error generating session ID:', error);
        }
      }
      fetchSessionId();
    }
  }, []);

  return (
    <>
    <Search webSearch={webSearch} setWebSearch={setWebSearch}/>
    <MessageDisplay
    messages={messages}
    />
    <ChatInput
    setMessage={setMessages}
    allMessages={messages}
    webSearch={webSearch}
    />
    </>
  )
}

async function getSessionId(){
    let sessionId;
    try{
        sessionId = await axios.post('http://127.0.0.1:8000/sessionIdGen');
        console.log(sessionId.data.sessionId);
    }catch(error){
        console.error('Error generating session ID:', error);
    }
    return sessionId.data.sessionId;
}

