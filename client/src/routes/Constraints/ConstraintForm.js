import React, { useState } from "react";

const ConstraintForm = ({ createConstraint, onAdd }) => {
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const constraint = await createConstraint(file);
    onAdd(constraint);
  };

  const handleChange = (e) => setFile(e.target.files[0]);

  return (
    <form onSubmit={handleSubmit} enctype="multipart/form-data">
      <p>Create a constraint</p>
      <input
        onChange={handleChange}
        name="json_file"
        type="file"
        accept="application/json"
      />
      <button type="submit">Add</button>
    </form>
  );
};

export default ConstraintForm;
