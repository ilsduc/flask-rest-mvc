import React, { Suspense } from "react";
import { Redirect } from "react-router-dom";

const HomePageRoute = React.lazy(() => import("./routes/Home"));
const ConstraintsPageRoute = React.lazy(() => import("./routes/Constraints"));

const routes = {
  home: {
    path: "/",
    Component: () => (
      <Suspense fallback="Loading ...">
        <HomePageRoute />
      </Suspense>
    ),
  },
  constraints: {
    path: "/constraints",
    Component: () => (
      <Suspense fallback="Loading ...">
        <ConstraintsPageRoute />
      </Suspense>
    ),
  },
  notFound: {
    path: "*",
    Component: () => (
      <Suspense fallback="Loading ...">
        <Redirect to="/" />
      </Suspense>
    ),
  },
};

export default routes;
