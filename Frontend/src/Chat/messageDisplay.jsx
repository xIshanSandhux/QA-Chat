import './messagedisplay.css'
// import assistant from './assistant.png'
import { TbMessageChatbot } from "react-icons/tb";
import { FaRegUserCircle } from "react-icons/fa";
export default function MessageDisplay(){

    const messageTemp = [
        {"role":"user","message":"Hello How are you"},
        {"role":"assistant","message":"I amffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddd ffffffffffffffffffffffffffffffffffffffffff good how are you"},
        {"role":"user","message":"What kind of chat are you"},
        {"role":"assistant","message":"I adddd dddddd fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff dddddddddddd dddddddddddddddddddddddddddddd ddddddddddddddddddddddddddddd dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccccccccc ccccccccccccccccccddddddddddddddddddddddddddddddm a gemini powered RAG Chatbot, here to help you answer questions based on the pdf uploaded by you"},
    ];

    return (
        <div>
            {messageTemp.map(({role,message},index)=>(
                <div key={index} className="message-container">
                   {

                  ( role==="user")
                    ?
                    <div className='text-container'>
                        <div className='text-icon'>
                            <FaRegUserCircle size={30} color="white" />
                        </div>
                        {message}</div>
                : <div className='text-container'>
                    <div className='text-icon'>
                        <TbMessageChatbot size={31} color="white" />
                    </div>
                    {message}
                    </div>
                   }
                </div>
            ))}
        </div>
    );
}