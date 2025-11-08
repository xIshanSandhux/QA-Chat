import './messagedisplay.css'
import { TbMessageChatbot } from "react-icons/tb";
import { FaRegUserCircle } from "react-icons/fa";
import {useEffect, useRef} from 'react';
export default function MessageDisplay({messages}){
   const chatRef = useRef(null);

   useEffect(()=>{
    if(chatRef.current){
        chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
   }, [messages]);
   
    return (
        <div className='chat' ref={chatRef}>
            {messages.map(({role,message},index)=>(
                <div key={index} className="message-container">
                   {( role==="user")?
                   <div className='text-container'>
                    <div className='text-icon'>
                        <FaRegUserCircle size={30} color="white" />
                        </div>
                        {message}
                        </div>
                    : <div className='text-container'>
                        <div className='text-icon'>
                            <TbMessageChatbot size={31} color="white" /></div>
                        {message}
                        </div>
                    }
                    </div>
                ))}
            </div>
        );
}