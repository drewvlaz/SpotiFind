import React, { useEffect, useState, Fragment } from 'react';
import axios from 'axios';
import { Button, Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function SingleLabel({ label, index, toggleLabel }) {
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

const Labels = () => {
  const [labels, setLabels] = useState([]);

  const createLabels = (rawData) => {
    const newLabels = [];
    for (const element of rawData) {
      newLabels.push({'label': element, 'selected': true});
    }
    newLabels.push({'label': 'Select all', 'selected': true})
    setLabels(newLabels);
  };

  const toggleLabel = (index) => {
    const newLabels = [...labels];
    const currSelectedState = newLabels[newLabels.length-1].selected;
    if (index === newLabels.length-1) {
      for (let i=0; i<newLabels.length; i++) {
        newLabels[i].selected = !currSelectedState;
      }
    }
    else {
      newLabels[index].selected = !newLabels[index].selected;
      if (!newLabels[index].selected) {
        newLabels[newLabels.length-1].selected = false;
      }
    }
    setLabels(newLabels);
  }

  const sendAuthToken = async (payload) => {
    await axios
    .post("http://localhost:5000/flask/auth", payload)
    .then((res) => console.log(res));
  };

  const sendLabels = async (payload) => {
    await axios
    .post("http://localhost:5000/flask/labels", payload)
    .then((res) => console.log(res));
  };


  useEffect(() => {
    const authToken = window.location.hash.split("=")[1].split("&")[0];
    console.log(authToken);
    const payload = { authToken: authToken }
    sendAuthToken(payload);
    const fetchData = async () => {
      await axios
        .get('./data.json')
        .then((res) => createLabels(res.data.labels))
        .catch((err) => console.log(err))
    }
    fetchData();
  }, []);

  const handleSubmit = () => {
    const returnLabels = [];
    for (const element of labels) {
      console.log(element.selected);
      if (element.selected) {
        returnLabels.push(element.label);
      }
    }
    const payload = { labels: returnLabels };
    console.log(payload);
    sendLabels(payload);
  };

  // TODO: Create group for moods and group for keywords
  return (
    <Fragment>
      <div className="container mt-2">
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
        </div>
      </div>
      <br></br>
    </Fragment>
  );
};

export default Labels;
