import React, { useEffect, useState, Fragment } from 'react';
import axios from 'axios';
import { Button, Card, Form } from 'react-bootstrap';
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
    const _labels = [];
    for (const element of rawData) {
      _labels.push({'label': element, 'selected': true});
    }
    _labels.push({'label': 'Select all', 'selected': true})
    setLabels(_labels);
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

  const handleSubmit = () => {

  };

  useEffect(() => {
    const fetchData = async () => {
      await axios
        .get('./data.json')
        .then((res) => createLabels(res.data.labels))
        .catch((err) => console.log(err))
    }
    fetchData();
  }, []);


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
          <Button variant="outline-dark mb-6" size="large" onClick={handleSubmit}>
            Generate Playlist
          </Button>
        </div>
      </div>
      <br></br>
    </Fragment>
  );
};

export default Labels;
