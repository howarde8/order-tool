import React, { useState } from 'react';
import { Layout, Menu, Typography } from 'antd';
import {
  SettingOutlined,
  MenuUnfoldOutlined,
  MenuFoldOutlined
} from '@ant-design/icons';

const DEFAULT_COLLAPSED_WIDTH = 80;
const TRIGGERED_COLLAPSED_WIDTH = 0;

function Buyer() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Layout.Sider
        trigger={null}
        breakpoint="lg"
        onBreakpoint={broken => setCollapsed(broken)}
        collapsible
        collapsed={collapsed}
        collapsedWidth={
          collapsed ? TRIGGERED_COLLAPSED_WIDTH : DEFAULT_COLLAPSED_WIDTH
        }
      >
        <div
          style={{
            height: '32px',
            margin: '16px'
          }}
        >
          <Typography.Title
            style={{ textAlign: 'center', color: '#ccc' }}
            level={3}
          >
            OT
          </Typography.Title>
        </div>
        <Menu theme="dark">
          <Menu.Item>
            <SettingOutlined />
            <span>Setting</span>
          </Menu.Item>
        </Menu>
      </Layout.Sider>
      <Layout>
        <Layout.Header style={{ background: '#fff' }}>
          {React.createElement(
            collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
            {
              onClick: () => setCollapsed(!collapsed)
            }
          )}
        </Layout.Header>
      </Layout>
    </Layout>
  );
}

export default Buyer;
