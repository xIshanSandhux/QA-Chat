import { useEffect, useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import ChatInput from './input';
import MessageDisplay from './messageDisplay';
import Search from '../webSearch/search';
import UploadButton from '../fileUpload/uploadButton';

let ran = false;
export default function ChatMain(){

  const [messages, setMessages] = useState([]);
  const [rag, setRag] = useState(false);
  const [uploadSessionId, setUploadSessionId] = useState(null);
  console.log(rag);

    useEffect(()=>{
    // let sessionId;
    if (!ran){
      ran = true;
      const fetchSessionId = async () => {
        // let sessionId;
        try{
          const sessionId = await getSessionId();
          Cookies.set('sessionId', sessionId);
          setUploadSessionId(sessionId);
        }catch(error){
          console.error('Error generating session ID:', error);
        }
      }
      fetchSessionId();
    }
  }, []);

  return (
    <>
    <UploadButton sessionId={uploadSessionId}/>
    <Search rag={rag} setRag={setRag}/>
    <MessageDisplay
    messages={messages}
    />
    <ChatInput
    setMessage={setMessages}
    allMessages={messages}
    rag={rag}
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

