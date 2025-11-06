import './messagedisplay.css'
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
                <div className="message-container">
                   {

                  ( role==="user")
                    ?
                    <div className='user-container'>{"User: " + message}</div>
                : <div className='assistant-container'>{"Assitant: "+ message}</div>
                   }
                </div>
                
                
            ))}
        </div>
    );
}