import React from 'react';
import { Layout, Row, Col, Typography, Form, Input, Button } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';

function Login(props) {
  const onFinish = (values) => {
    props.login(values);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Layout.Content style={{ padding: '5%' }}>
        <Form onFinish={onFinish}>
          <Typography.Title
            style={{ textAlign: 'center', color: 'grey' }}
            level={3}
          >
            Order Tool
          </Typography.Title>
          <Row justify="center">
            <Col xs={22} sm={16} md={8}>
              <Form.Item
                style={{ width: '100%' }}
                name="username"
                rules={[
                  {
                    required: true,
                    message: 'Please input your username!',
                  },
                ]}
              >
                <Input
                  size="large"
                  placeholder="Username"
                  prefix={<UserOutlined />}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row justify="center">
            <Col xs={22} sm={16} md={8}>
              <Form.Item
                style={{ width: '100%' }}
                name="password"
                rules={[
                  {
                    required: true,
                    message: 'Please input your password!',
                  },
                ]}
              >
                <Input.Password
                  size="large"
                  placeholder="Password"
                  prefix={<LockOutlined />}
                />
              </Form.Item>
            </Col>
          </Row>
          <Row justify="center">
            <Col xs={22} sm={16} md={8}>
              <Form.Item>
                <Button
                  style={{ width: '100%' }}
                  size="large"
                  type="primary"
                  htmlType="submit"
                >
                  Login
                </Button>
              </Form.Item>
            </Col>
          </Row>
        </Form>
      </Layout.Content>
    </Layout>
  );
}

export default Login;
