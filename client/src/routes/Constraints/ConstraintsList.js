import React from "react";

const ConstraintsList = ({ constraints }) => {
  return (
    <ul>
      {constraints.map((constraintName) => (
        <li>{constraintName}</li>
      ))}
    </ul>
  );
};

export default ConstraintsList;
