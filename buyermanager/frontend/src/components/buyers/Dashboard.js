import React, { Fragment } from "react";
import Form from "./Form";
import Buyers from "./Buyers";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Buyers />
    </Fragment>
  );
}