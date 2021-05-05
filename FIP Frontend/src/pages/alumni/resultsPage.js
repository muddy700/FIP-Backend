import React from 'react'
import { Table } from 'react-bootstrap'

const ResultsPage = () => {
    return (
        <Table striped bordered hover responsive className="table-sm">
  <thead>
    <tr>
      <th>S/N</th>
      <th>Organization</th>
      <th>Address</th>
      <th>Professions</th>
      <th>Status</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
      <td>@mdo</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
      <td>@fat</td>
      <td>@fat</td>
    </tr>
    <tr>
      <td>3</td>
      <td colSpan="2">Larry the Bird</td>
      <td>@twitter</td>
      <td>@twitter</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</Table>
    )
}

export default ResultsPage
