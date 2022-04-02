import React, { useEffect, useState, Fragment } from 'react';

const Labels = () => {
  const [data, setData] = useState([]);
  const getData = () => {
    fetch(
      './data.json',
      {
        headers : { 
          'Content-Type': 'application/json',
          'Accept': 'application/json'
         }
      }
    )
    .then(function(response){
      console.log(response)
      return response.json();
    })
    .then(function(myJson) {
      console.log(myJson);
      setData(myJson);
    });
  };

  useEffect(()=>{
    getData()
  },[]);

  console.log(data.length);

  return (
    <Fragment>
      <div className="container mt-2">
        <h1>Sorting</h1>
        {
         data && data.length > 0 && data.map((item) => <p>{item.labels}</p>)
        }
      </div>
    </Fragment>
  );
};

export default Labels;
