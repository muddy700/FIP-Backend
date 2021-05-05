import React from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import { LoginPage } from './pages/loginPage'
import { HomePage } from './pages/mainPage';
import { PageNotFound } from './pages/pageNotFound';

export const App = () => {

    return (
    <Router>
      <div className="app">
        <div className="app-container">
            <Switch>
              <Route exact path="/login">
                <LoginPage />
              </Route>
              <Route exact path={["/home", "/"]}>
                <HomePage />
              </Route>
              <Route path="*">
                <PageNotFound />
              </Route>
            </Switch> 
        </div>
      </div>
    </Router>
    );
  }