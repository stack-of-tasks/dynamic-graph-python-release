// Copyright 2011, 2012, Florent Lamiraux, LAAS-CNRS.

#include <dynamic-graph/pool.h>
#include <dynamic-graph/entity.h>
#include <vector>

#include "dynamic-graph/python/exception.hh"
#include "dynamic-graph/python/dynamic-graph-py.hh"

namespace dynamicgraph {
namespace python {

#if PY_MAJOR_VERSION == 2
extern PyObject* dgpyError;
#endif

namespace pool {

PyObject* writeGraph(
#if PY_MAJOR_VERSION >= 3
    PyObject* m, PyObject* args
#else
    PyObject*, PyObject* args
#endif
) {
  char* filename;
  if (!PyArg_ParseTuple(args, "s", &filename)) return NULL;
  try {
    PoolStorage::getInstance()->writeGraph(filename);
  }
  CATCH_ALL_EXCEPTIONS(m);
  return Py_BuildValue("");
}

/**
   \brief Get list of entities
*/
PyObject* getEntityList(
#if PY_MAJOR_VERSION >= 3
    PyObject* m, PyObject* args
#else
    PyObject*, PyObject* args
#endif
) {
  if (!PyArg_ParseTuple(args, "")) return NULL;

  std::vector<std::string> entityNames;
  try {
    const PoolStorage::Entities& listOfEntities = dynamicgraph::PoolStorage::getInstance()->getEntityMap();

    Py_ssize_t classNumber = listOfEntities.size();
    // Build a tuple object
    PyObject* classTuple = PyTuple_New(classNumber);

    Py_ssize_t iEntity = 0;
    for (PoolStorage::Entities::const_iterator entity_it = listOfEntities.begin(); entity_it != listOfEntities.end();
         ++entity_it) {
      const std::string& aname = entity_it->second->getName();

      PyObject* className = Py_BuildValue("s", aname.c_str());
      PyTuple_SetItem(classTuple, iEntity, className);
      iEntity++;
    }
    return Py_BuildValue("O", classTuple);
  }
  CATCH_ALL_EXCEPTIONS(m);
  return NULL;
}

}  // namespace pool
}  // namespace python
}  // namespace dynamicgraph
