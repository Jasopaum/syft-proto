// DO NOT EDIT.
//
// Generated by the Swift generator plugin for the protocol buffer compiler.
// Source: syft_proto/execution/v1/plan.proto
//
// For information on using the generated types, please see the documentation:
//   https://github.com/apple/swift-protobuf/

import Foundation
import SwiftProtobuf

// If the compiler emits an error on this type, it is because this file
// was generated by a version of the `protoc` Swift plug-in that is
// incompatible with the version of SwiftProtobuf to which you are linking.
// Please ensure that you are building against the same version of the API
// that was used to generate this file.
fileprivate struct _GeneratedWithProtocGenSwiftVersion: SwiftProtobuf.ProtobufAPIVersionCheck {
  struct _2: SwiftProtobuf.ProtobufAPIVersion_2 {}
  typealias Version = _2
}

struct SyftProto_Execution_V1_Plan {
  // SwiftProtobuf.Message conformance is added in an extension below. See the
  // `Message` and `Message+*Additions` files in the SwiftProtobuf library for
  // methods supported on all messages.

  var id: SyftProto_Types_Syft_V1_Id {
    get {return _id ?? SyftProto_Types_Syft_V1_Id()}
    set {_id = newValue}
  }
  /// Returns true if `id` has been explicitly set.
  var hasID: Bool {return self._id != nil}
  /// Clears the value of `id`. Subsequent reads from it will return its default value.
  mutating func clearID() {self._id = nil}

  var role: SyftProto_Execution_V1_Role {
    get {return _role ?? SyftProto_Execution_V1_Role()}
    set {_role = newValue}
  }
  /// Returns true if `role` has been explicitly set.
  var hasRole: Bool {return self._role != nil}
  /// Clears the value of `role`. Subsequent reads from it will return its default value.
  mutating func clearRole() {self._role = nil}

  var includeState: Bool = false

  var name: String = String()

  var tags: [String] = []

  var description_p: String = String()

  var torchscript: Data = SwiftProtobuf.Internal.emptyData

  var inputTypes: SyftProto_Execution_V1_NestedTypeWrapper {
    get {return _inputTypes ?? SyftProto_Execution_V1_NestedTypeWrapper()}
    set {_inputTypes = newValue}
  }
  /// Returns true if `inputTypes` has been explicitly set.
  var hasInputTypes: Bool {return self._inputTypes != nil}
  /// Clears the value of `inputTypes`. Subsequent reads from it will return its default value.
  mutating func clearInputTypes() {self._inputTypes = nil}

  var unknownFields = SwiftProtobuf.UnknownStorage()

  init() {}

  fileprivate var _id: SyftProto_Types_Syft_V1_Id? = nil
  fileprivate var _role: SyftProto_Execution_V1_Role? = nil
  fileprivate var _inputTypes: SyftProto_Execution_V1_NestedTypeWrapper? = nil
}

// MARK: - Code below here is support for the SwiftProtobuf runtime.

fileprivate let _protobuf_package = "syft_proto.execution.v1"

extension SyftProto_Execution_V1_Plan: SwiftProtobuf.Message, SwiftProtobuf._MessageImplementationBase, SwiftProtobuf._ProtoNameProviding {
  static let protoMessageName: String = _protobuf_package + ".Plan"
  static let _protobuf_nameMap: SwiftProtobuf._NameMap = [
    1: .same(proto: "id"),
    2: .same(proto: "role"),
    3: .standard(proto: "include_state"),
    4: .same(proto: "name"),
    5: .same(proto: "tags"),
    6: .same(proto: "description"),
    7: .same(proto: "torchscript"),
    8: .standard(proto: "input_types"),
  ]

  mutating func decodeMessage<D: SwiftProtobuf.Decoder>(decoder: inout D) throws {
    while let fieldNumber = try decoder.nextFieldNumber() {
      switch fieldNumber {
      case 1: try decoder.decodeSingularMessageField(value: &self._id)
      case 2: try decoder.decodeSingularMessageField(value: &self._role)
      case 3: try decoder.decodeSingularBoolField(value: &self.includeState)
      case 4: try decoder.decodeSingularStringField(value: &self.name)
      case 5: try decoder.decodeRepeatedStringField(value: &self.tags)
      case 6: try decoder.decodeSingularStringField(value: &self.description_p)
      case 7: try decoder.decodeSingularBytesField(value: &self.torchscript)
      case 8: try decoder.decodeSingularMessageField(value: &self._inputTypes)
      default: break
      }
    }
  }

  func traverse<V: SwiftProtobuf.Visitor>(visitor: inout V) throws {
    if let v = self._id {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 1)
    }
    if let v = self._role {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 2)
    }
    if self.includeState != false {
      try visitor.visitSingularBoolField(value: self.includeState, fieldNumber: 3)
    }
    if !self.name.isEmpty {
      try visitor.visitSingularStringField(value: self.name, fieldNumber: 4)
    }
    if !self.tags.isEmpty {
      try visitor.visitRepeatedStringField(value: self.tags, fieldNumber: 5)
    }
    if !self.description_p.isEmpty {
      try visitor.visitSingularStringField(value: self.description_p, fieldNumber: 6)
    }
    if !self.torchscript.isEmpty {
      try visitor.visitSingularBytesField(value: self.torchscript, fieldNumber: 7)
    }
    if let v = self._inputTypes {
      try visitor.visitSingularMessageField(value: v, fieldNumber: 8)
    }
    try unknownFields.traverse(visitor: &visitor)
  }

  static func ==(lhs: SyftProto_Execution_V1_Plan, rhs: SyftProto_Execution_V1_Plan) -> Bool {
    if lhs._id != rhs._id {return false}
    if lhs._role != rhs._role {return false}
    if lhs.includeState != rhs.includeState {return false}
    if lhs.name != rhs.name {return false}
    if lhs.tags != rhs.tags {return false}
    if lhs.description_p != rhs.description_p {return false}
    if lhs.torchscript != rhs.torchscript {return false}
    if lhs._inputTypes != rhs._inputTypes {return false}
    if lhs.unknownFields != rhs.unknownFields {return false}
    return true
  }
}
