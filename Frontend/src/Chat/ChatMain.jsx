import { useEffect } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';


let ran = false;
export default function ChatMain(){

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

