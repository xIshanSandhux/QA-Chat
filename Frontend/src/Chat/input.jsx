export default function ChatInput(){
    return (
        <div className="chat-input">
            <h1>Chat Input</h1>
            <input type="text" placeholder="Type your message here..." />
            <button onClick={() => onSend({message: "Sending message..."})}>Send</button>
    </div>
  );
}

function onSend(props){
    return(
        alert(props.message)
    )
}