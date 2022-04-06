import React, { useEffect, useState, Fragment } from 'react';
import axios from 'axios';
import { Button, Card, Form } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { makeStyles } from '@material-ui/core/styles';
// import axios from 'axios';
// import { Button } from 'react-bootstrap'

const useStyles = makeStyles({
    login: {
        display: 'grid',
        placeItems: 'center',
        height: '20vh',

        '& a':{
          padding: '20px',
          borderRadius: '99px',
          backgroundColor: '#1db954',
          fontWeight: 600,
          color: 'white',
          textDecoration: 'none',
          position: 'bottom',
          bottom: 0,
        },

        '& a:hover':{
          backgroundColor:' white',
          borderColor: '#1db954',
          color: '#1db954',
        }
    },
});

const SingleLabel = ({ label, index, toggleLabel }) => {
  let button;

  if (!label.selected) {
    button = <Button variant="outline-dark" outline="primary" onClick={() => toggleLabel(index)}>✕</Button>;
  }
  else {
    button = <Button variant="outline-success" onClick={() => toggleLabel(index)}>✓</Button>;
  }

      // <span style={{ textDecoration: label.selected ? "line-through" : "" }}>{label.label}</span>
      // <div className="container mt-2" onClick={() => toggleLabel(index)}>
  return (
    <div className="container mt-2">
      <Card border={label.selected ? "success" : "dark"}>
        <Card.Body>
          <div className="label">
            <span>{label.label}</span>
            <div>
              {button}
            </div>
          </div>
        </Card.Body>
      </Card>
    </div>
  );
}


const FormLabel = ({ addLabel }) => {
  const [value, setValue] = React.useState("");

  const handleSubmit = e => {
    e.preventDefault();
    if (!value) return;
    addLabel(value);
    setValue("");
  };

  return (
    <Form onSubmit={handleSubmit}> 
    <Form.Group>
      <Form.Label><b>Add Keyword</b></Form.Label>
      <Form.Control type="text" className="input" value={value} onChange={e => setValue(e.target.value)} placeholder="Add new keyword" />
    </Form.Group>
    <div className="container mt-2 text-center d-grid gap-2">
      <Button variant="outline-dark mb-6" size="large" type="submit">
          Add
      </Button>
    </div>
  </Form>
  );
}

const GoToPlaylist = ({ link }) => {
  const classes = useStyles();
  if (link.active) {
    return (
      <div className={classes.login}>
        <a href={link.link}>GO TO PLAYLIST</a>
      </div>
    );
  }
  else {
    return null;
  }
}


const Labels = () => {
  const [labels, setLabels] = useState([]);
  const [link, setLink] = useState({link: "", active: false});

  const createLabels = (rawData) => {
    const newLabels = [];
    for (const element of rawData) {
      newLabels.push({'label': element, 'selected': true});
    }
    // newLabels.push({'label': 'Select all', 'selected': true})
    setLabels(newLabels);
  };

  const toggleLabel = (index) => {
    const newLabels = [...labels];
    const currSelectedState = newLabels[newLabels.length-1].selected;
    // if (index === newLabels.length-1) {
    //   for (let i=0; i<newLabels.length; i++) {
    //     newLabels[i].selected = !currSelectedState;
    //   }
    // }
    // else {
      newLabels[index].selected = !newLabels[index].selected;
      // if (!newLabels[index].selected) {
      //   newLabels[newLabels.length-1].selected = false;
      // }
    // }
    setLabels(newLabels);
  }

  const addLabel = (text) => {
      const newLabels = [...labels, { label: text, selected: true }];
      setLabels(newLabels);
  };

  const removeLabel = (index) => {
    const newLabels = [...labels];
    newLabels.splice(index, 1);
    setLabels(newLabels);
  };


  const sendAuthToken = async (payload) => {
    await axios
    .post("http://localhost:5000/flask/auth", payload)
    .then((res) => console.log(res));
  };

  const sendLabels = async (payload) => {
    await axios
    .post("http://localhost:5000/flask/labels", payload)
    .then((res) => setLink({ link: res.data.message, active: true}));
  };

  // useEffect(() => {
  //   // const authToken = window.location.hash.split("=")[1].split("&")[0];
  //   // console.log(authToken);
  //   // const payload = { authToken: authToken }
  //   // sendAuthToken(payload);
  //   const fetchData = async () => {
  //     await axios
  //       .get('./data.json')
  //       .then((res) => createLabels(res.data.labels))
  //       .catch((err) => console.log(err))
  //   }
  //   fetchData();
  // }, []);

  const handleSubmit = () => {
    const authToken = window.location.hash.split("=")[1].split("&")[0];
    console.log(authToken);
    // const payload = { authToken: authToken }
    // sendAuthToken(payload)

    const returnLabels = [];
    for (const element of labels) {
      console.log(element.selected);
      if (element.selected) {
        returnLabels.push(element.label);
      }
    }
    const payload = { labels: returnLabels, authToken: authToken };
    console.log(payload);
    sendLabels(payload);
  };

  // TODO: Create group for moods and group for keywords
  return (
    <Fragment>
    <div className="container mt-4">
      <h1 className="text-center mb-4">Keywords List</h1>
        <div className="container mt-4">
          <FormLabel addLabel={addLabel} />
        </div>
        <div className="container mt-4">
          {labels.map((label, index) => (
            <SingleLabel 
              label={label}
              index={index}
              toggleLabel={toggleLabel}
            />
          ))}
          <div className="container mt-3 text-center d-grid gap-2">
            <Button variant="outline-dark mb-6" size="large" onClick={() => handleSubmit()}>
              Generate Playlist
            </Button>
            <GoToPlaylist link={link}/>
          </div>
        </div>
      </div>
      <br></br>
    </Fragment>
  );
};

export default Labels;
