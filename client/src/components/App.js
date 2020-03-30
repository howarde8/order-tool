import React from 'react';
import { Layout } from 'antd';
import Login from './Login';

function App() {
  return (
    <div>
      <Layout style={{ height: '100vh' }}>
        <Layout.Content style={{ padding: '5%' }}>
          <Login />
        </Layout.Content>
      </Layout>
    </div>
  );
}

export default App;
