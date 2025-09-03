import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import CardText from 'react-bootstrap/esm/CardText';

function LocationCard(props) {
    let locationName = props.locationName;
    let locationImage = props.locationImage;
    let xCoord = props.xCoord;
    let yCoord = props.yCoord;
    let zCoord = props.zCoord;
    let dimension = props.dimension;
    let notes = props.notes;
    let lastEdited = props.lastEdited;
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={locationImage} width="200" height="200"/>
      <Card.Body>
        <Card.Title>{locationName}</Card.Title>
        <Card.Text>
            Coordenates: {xCoord}, {yCoord}, {zCoord}
        </Card.Text>
        <CardText>
            Dimension: {dimension}
        </CardText>
        <CardText>
            Notes: {notes}
        </CardText>
        <CardText>
            Last edited: {lastEdited}
        </CardText>
        <Button variant="primary">More</Button>
      </Card.Body>
    </Card>
  );
}

export default LocationCard