/**
 * PersonView view component.
 * @module components/View/PersonView
 */

import React from 'react';
import { Grid, Card, Image, List, Segment } from 'semantic-ui-react';
import PropTypes from 'prop-types';
import EmailWidget from '@plone/volto/components/theme/Widgets/EmailWidget';

const PreviewImage = ({ content }) => {
  const { image, image_caption } = content;
  const scale_name = 'preview';
  const scale = image.scales[scale_name];
  const { download, heigth, width } = scale;
  return (
    <Image
      src={download}
      alt={image_caption}
      height={heigth}
      size={width}
    ></Image>
  );
};
/**
 * PersonView view component class.
 * @function PersonView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PersonView = (props) => {
  const { content } = props;

  return (
    <Segment>
      <Grid columns={2} divided>
        <Grid.Row>
          <Grid.Column>
            <Card fluid>
              {content.image && (
                <div className="image">
                  <PreviewImage content={content} />
                </div>
              )}
              <Card.Content>
                {content.description && (
                  <Card.Description>{content.description}</Card.Description>
                )}
              </Card.Content>
              <Card.Content extra>
                <div>
                  {content.email && (
                    <div>
                      <EmailWidget value={content.email} />
                    </div>
                  )}
                </div>
                <div>
                  {content.extension && <div>Ramal: {content.extension}</div>}
                </div>
              </Card.Content>
            </Card>
          </Grid.Column>
          <Grid.Column>
            <Card fluid>
              <Card.Content>
                <Card.Header>Campus</Card.Header>
                <Card.Description extra>
                  {content.campus.map((campus) => (
                    <List divided relaxed>
                      <List.Item>
                        <List.Icon name="institution" />

                        <List.Content>
                          <List.Header as="a">
                            <a href={campus['@id']}>{campus.title}</a>
                          </List.Header>
                        </List.Content>
                      </List.Item>
                    </List>
                  ))}
                </Card.Description>
              </Card.Content>
            </Card>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Segment>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
PersonView.propTypes = {
  content: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    image: PropTypes.object,
    campus: PropTypes.array,
    email: PropTypes.string.isRequired,
    extension: PropTypes.string.isRequired,
  }).isRequired,
};

export default PersonView;
