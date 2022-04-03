import React, { useEffect } from 'react';
import 'react-dropzone-uploader/dist/styles.css'
import Dropzone from 'react-dropzone-uploader'
import { getDroppedOrSelectedFiles } from 'html5-file-selector';
import axios from 'axios';
// import ResultPage from './ResultPage';


const UploadImage = () => {
    //add the add file tag to our program
    // limit to image file types
    //event handler that listens to changes
    //send received image file to server
    //
    // add image to file
    //make whole space clickable
    // make it say upload image here
    //click or drag and drop to upload image
    //don't worry about protecting against other types of files

    const fileParams = ({ meta }) => {
        return { url: 'https://httpbin.org/post' }
    };
    const onFileChange = ({ meta, file }, status) => { 
        console.log(status, meta, file) 
    };

    const sendImageUrl = async (payload) => {
      await axios
      .post("http://localhost:5000/flask/upload", payload)
      .then((res) => console.log(res));
    };

    // const navigate = useNavigate();
    const onSubmit = (files, allFiles) => {
        // console.log("HERE");
        console.log(files);
        // console.log("HERE");
        const payload = { imageUrl: files[0]["meta"]["previewUrl"] }
        sendImageUrl(payload);
        // navigate('/labels');
        // allFiles.forEach(f => f.remove())
    };
    const getFilesFromEvent = e => {
        return new Promise(resolve => {
            getDroppedOrSelectedFiles(e).then(chosenFiles => {
                resolve(chosenFiles.map(f => f.fileObject))
            })
        })
    }

  const sendAuthToken = async (payload) => {
    await axios
    .post("http://localhost:5000/flask/auth", payload)
    .then((res) => console.log(res));
  };

  useEffect(() => {
    const authToken = window.location.hash.split("=")[1].split("&")[0];
    console.log(authToken);
    const payload = { authToken: authToken }
    sendAuthToken(payload);
  }, []);

    const selectFileInput = ({ accept, onFiles, files, getFilesFromEvent }) => {
        const textMsg = files.length > 0 ? 'Upload Again' : 'Click here or drag and drop to upload image'
        return (
            <label className="btn btn-danger mt-4">
               
                <input
                    style={{ display: 'none' }}
                    type="file"
                    accept={accept}
                    multiple
                    onChange={e => {
                        getFilesFromEvent(e).then(chosenFiles => {
                            onFiles(chosenFiles)
                        })
                    }}
                />
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <p1>{textMsg}</p1> 
            </label>
        )
    }
    return (
        <Dropzone
            onSubmit={onSubmit}
            onChangeStatus={onFileChange}
            InputComponent={selectFileInput}
            getUploadParams={fileParams}
            getFilesFromEvent={getFilesFromEvent}
            //only accept image
            accept="image/*"
            //change to 1 file
            maxFiles={1}
            inputContent="Drop A File"
            styles={{
                dropzone: { width: 600, height: 400, outline: 'none', },
                dropzoneActive: { 
                    borderColor: '#1db954',
                    backgroundColor: '#1db954',
                    
             },
            }}            
        />
    );
};

export default UploadImage;
