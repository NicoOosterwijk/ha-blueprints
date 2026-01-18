#--------------------------------------------------------------------------------------------------
# Set the state or other attributes for the entity specified in the Automation Action
#--------------------------------------------------------------------------------------------------

inputEntity = data.get('entity_id')
inputStateObject = hass.states.get(inputEntity)
inputState = inputStateObject.state
inputAttributesObject = inputStateObject.attributes.copy()

newState = data.get('state')
if newState is not None:
    inputState = newState

newClass = data.get('device_class')
if newClass is not None:
    inputAttributesObject['device_class'] = newClass

hass.states.set(inputEntity, inputState, inputAttributesObject)
