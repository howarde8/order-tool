import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Login from './Login';
import Buyer from './Buyer';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/">
          <Login />
        </Route>
        <Route path="/buyer">
          <Buyer />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
