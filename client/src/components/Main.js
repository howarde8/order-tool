import React from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import { Switch, Route } from 'react-router-dom';
import { message } from 'antd';

import Login from './Login';
import Buyer from './Buyer';

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null,
    };
  }

  componentDidMount = async () => {
    this.setState({ user: false });
    const token = Cookies.get('token');
    if (token) {
      try {
        const {
          data: { user },
        } = await axios.post('/api/token/verify/', { token });
        this.setState({ user });
        this.props.history.push('/buyer');
      } catch (err) {
        this.setState({ user: null });
        this.props.history.push('/');
      }
    }
  };

  login = async ({ username, password }) => {
    try {
      const {
        data: { token, user },
      } = await axios.post('/api/token/obtain/', { username, password });
      Cookies.set('token', token);
      this.setState({ user });
      this.props.history.push('/buyer');
      message.success('Login successful');
    } catch (err) {
      message.error('Login failed');
    }
  };

  logout = () => {
    this.setState({ user: null });
    Cookies.remove('token');
    this.props.history.push('/');
    message.success('Logout successful');
  };

  render() {
    return (
      <Switch>
        <Route exact path="/">
          <Login login={this.login} />
        </Route>
        <Route path="/buyer">
          <Buyer user={this.state.user} logout={this.logout} />
        </Route>
      </Switch>
    );
  }
}

export default Main;
