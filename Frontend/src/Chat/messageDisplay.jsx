import './messagedisplay.css'
import { TbMessageChatbot } from "react-icons/tb";
import { FaRegUserCircle } from "react-icons/fa";
export default function MessageDisplay({messages}){

    return (
        <div>
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