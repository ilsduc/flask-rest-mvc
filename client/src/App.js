import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import routes from "./routes";

function App() {
  return (
    <Router>
      <Switch>
        <Route
          exact
          path={routes.home.path}
          component={routes.home.Component}
        />
        <Route
          exact
          path={routes.constraints.path}
          component={routes.constraints.Component}
        />
        <Route
          exact
          path={routes.notFound.path}
          component={routes.notFound.Component}
        />
      </Switch>
    </Router>
  );
}

export default App;
