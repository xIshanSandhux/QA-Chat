export default function UploadButton(){

    const onClickButton = () => {
       
    }

    return (
        <div>
            <input type="file" display="none" />
            <button onClick={onClickButton}>Upload</button>
        </div>
    )
}