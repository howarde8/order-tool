import React, { useState } from 'react';
import { Layout, Menu } from 'antd';
import { SettingOutlined } from '@ant-design/icons';

const DEFAULT_COLLAPSED_WIDTH = 80;
const TRIGGERED_COLLAPSED_WIDTH = 0;

function Buyer() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Layout.Sider
        breakpoint="lg"
        onBreakpoint={broken => setCollapsed(broken)}
        collapsible
        collapsedWidth={
          collapsed ? TRIGGERED_COLLAPSED_WIDTH : DEFAULT_COLLAPSED_WIDTH
        }
      >
        <Menu theme="dark">
          <Menu.Item>
            <SettingOutlined />
            <span>Setting</span>
          </Menu.Item>
        </Menu>
      </Layout.Sider>
      {/* <Layout.Header></Layout.Header> */}
    </Layout>
  );
}

export default Buyer;
