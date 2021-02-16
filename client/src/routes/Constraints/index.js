import React, { useEffect, useState } from "react";
import ConstraintsList from "./ConstraintsList";
import config from "../../config.json";
import ConstraintForm from "./ConstraintForm";

const { apiUrl } = config;

const createConstraint = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch(`${apiUrl}/constraints`, {
    method: "POST",
    body: formData,
  });
  return await res.json();
};

const getConstraints = async () => {
  const res = await fetch(`${apiUrl}/constraints`);
  return await res.json();
};

const Constraints = () => {
  const [constraints, setConstraints] = useState([]);

  useEffect(() => {
    const callApi = async () => setConstraints(await getConstraints());
    callApi();
  }, []);

  const onAdd = (constraint) => {
    setConstraints([...constraints, constraint]);
  };

  return (
    <React.Fragment>
      <ConstraintsList constraints={constraints} />
      <ConstraintForm onAdd={onAdd} createConstraint={createConstraint} />
    </React.Fragment>
  );
};

export default Constraints;
